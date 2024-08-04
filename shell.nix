let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (python-pkgs: [
      python-pkgs.pynacl
      python-pkgs.pyyaml
      python-pkgs.aiohttp
      python-pkgs.aiosignal
      python-pkgs.async-timeout
      python-pkgs.attrs
      python-pkgs.bcrypt
      python-pkgs.certifi
      python-pkgs.cffi
      python-pkgs.chardet
      python-pkgs.charset-normalizer
      python-pkgs.colorzero
      python-pkgs.cryptography
      python-pkgs.discordpy
      python-pkgs.distro
      # python-pkgs.ffmpeg
      python-pkgs.frozenlist
      python-pkgs.idna
      python-pkgs.jsonschema
      python-pkgs.multidict
      python-pkgs.paramiko
      python-pkgs.pathspec
      python-pkgs.praw
      python-pkgs.prawcore
      python-pkgs.pycparser
      # python-pkgs.pymongo
      python-pkgs.pyrsistent
      python-pkgs.python-dotenv
      python-pkgs.requests
      python-pkgs.six
      python-pkgs.typing-extensions
      python-pkgs.update-checker
      # python-pkgs.ssh-import-id
      python-pkgs.urllib3
      python-pkgs.websocket-client
      python-pkgs.yamllint
      python-pkgs.yarl
      python-pkgs.youtube-dl
    ]))
  ];
}
