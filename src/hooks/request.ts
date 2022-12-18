export const useRequest = (url: string, options?: any) => {
    const resource = ref<string>(url)
    const response = ref<any>(null)
    const request = async () => {
        const { data } = await useFetch(resource, {
            refetch: true, ...options
        }).json()
        response.value = unref(data)
    }
    onMounted(request)
    return {
        resource,
        response,
        request
    }
}