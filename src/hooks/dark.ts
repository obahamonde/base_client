import { useTheme } from 'vuetify';

const theme = useTheme();

export const isDark = useDark()
export const toggleDark = () => {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    isDark.value = !isDark.value
}