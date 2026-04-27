[app]

# (str) Nome do app
title = AppPromo

# (str) Nome do pacote
package.name = apppromo

# (str) Domínio (pode deixar assim)
package.domain = org.test

# (str) Diretório do código
source.dir = .

# (list) Extensões incluídas
source.include_exts = py,png,jpg,jpeg,kv

# (list) Arquivos que NÃO entram
source.exclude_exts = spec

# (list) Dependências
requirements = python3,kivy,requests,pillow

# (str) Orientação
orientation = portrait

# (bool) Tela cheia
fullscreen = 0

# (list) Permissões Android
android.permissions = INTERNET

# (int) Versão do app
version = 1.0

# (str) Ícone (opcional)
#icon.filename = %(source.dir)s/icon.png

# (str) Tela de splash (opcional)
#presplash.filename = %(source.dir)s/splash.png

# (bool) Permitir tela rotacionar
android.allow_backup = True

# (int) API mínima
android.minapi = 21

# (int) API alvo
android.api = 33

# (int) NDK
android.ndk = 25b

# (bool) usar log
log_level = 2


[buildozer]

# (int) nível de log
log_level = 2

# (int) número de threads
warn_on_root = 1
