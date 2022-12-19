from api.services import CloudService
from typing import List, Dict, Optional, Any, Union, Tuple, Callable
from pydantic import BaseModel, Field, BaseConfig
from pydantic.fields import ModelField
from uuid import uuid4
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr

class Model(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True
        extra = "allow"
        orm_mode = True
        allow_population_by_field_name = True
                
    @property
    def db(self):
        cloud = CloudService()
        return cloud.database
    
    @property
    def table(self):
        return self.__class__.__name__.lower()+"s"
    
    @property
    def _id(self):
        fields: List[ModelField] = self.__fields__.values()
        for field in fields:
            if field.field_info.extra.get("pk"):
                return str(getattr(self, field.name))
    
    @property
    def pk(self):
        return self.__class__.__name__.lower()+"s"+f"#{self._id}"
                 
    @property
    def sk(self):
        sk = ""
        fields: List[ModelField] = self.__fields__.values()
        for field in fields:
            if field.field_info.extra.get("index"):
                sk += f"#{getattr(self, field.name)}"
        return sk  
    
    @classmethod
    def create_table(cls):
        db = cls.db.fget(cls.db)
        db.create_table(
            TableName=cls.__name__.lower()+"s",
            KeySchema=[
                {
                    "AttributeName": "pk",
                    "KeyType": "HASH"
                },  
                {
                    "AttributeName": "sk",
                    "KeyType": "RANGE"
                }
            ],
            AttributeDefinitions=[
                {
                    
                    "AttributeName": "pk",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "sk",
                    "AttributeType": "S"
                }
            ],
            BillingMode="PAY_PER_REQUEST"
        )
        
    def create_one(self):
        self.db.Table(self.table).put_item(
            Item={
                "pk": self.pk,
                "sk": self.sk,
                **self.dict()
            }
        )
        return self.dict()
    
    @classmethod
    def find_many(cls, field:str):
        db = cls.db.fget(cls.db)
        table = db.Table(cls.__name__.lower()+"s")
        return table.query(
            KeyConditionExpression=Key("pk").begins_with(cls.__name__.lower()+"s") & Key("sk").begins_with(f"#{field}")
        )["Items"]
        
    @classmethod
    def find_one(cls, fields:List[str]):
        db = cls.db.fget(cls.db)
        table = db.Table(cls.__name__.lower()+"s")
        return table.query(
            KeyConditionExpression=Key("pk").begins_with(cls.__name__.lower()+"s") & Key("sk").eq(f"#{'#'.join(fields)}")
        )["Items"]
        
    @classmethod
    def find_by(cls, field:str, value:str):
        db = cls.db.fget(cls.db)
        table = db.Table(cls.__name__.lower()+"s")
        return table.query(
            KeyConditionExpression=Key("pk").begins_with(cls.__name__.lower()+"s") & Key("sk").begins_with("#"),
            FilterExpression=Attr(field).contains(value)
        )["Items"]
        
    def update_one(self):
        self.db.Table(self.table).put_item(
            Item={
                "pk": self.pk,
                "sk": self.sk,
                **self.dict()
            }
        )
        return self.dict()
    
    def delete_one(self):
        self.db.Table(self.table).delete_item(
            Key={
                "pk": self.pk,
                "sk": self.sk
            }
        )
        return self.dict()