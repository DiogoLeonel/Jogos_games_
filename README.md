🐍 Cobra Game — Jogo da Cobrinha em Python
Bem-vindo ao Cobra Game, um clássico jogo da cobrinha desenvolvido em Python com foco em diversão, simplicidade e aprendizado. Este projeto foi criado por Diogo como parte de um portfólio de desenvolvimento de jogos voltado para estudo e diversão.

🎮 Funcionalidades
- Menu simplificado interativo com música
- Sons de efeito durante o jogo
- Sistema de pontuação com registro de recorde
- Interface gráfica simples e intuitiva
- Código modular dividido em arquivos: cobra_principal.py, cobra_menu.py, cobra_jogo.py

📁 Estrutura do Projeto
projeto/
├── cobra_principal.py       # Arquivo principal do jogo
├── cobra_menu.py            # Tela de menu
├── cobra_jogo.py              # Lógica do jogo
├── recorde.txt                   # Armazena nome e pontuação máxima
├── recursos/
    ├── musica/
    ├── sons/

🚀 Como executar
Requisitos:
- Python 3.10 ou superior
- Bibliotecas: pygame
Instalação:
pip install pygame

Execução:
python cobra_principal.py
🧱 Gerar Executável (.exe)
Para rodar o jogo em qualquer computador com Windows:
pyinstaller --onefile --windowed --add-data "recursos;recursos" --add-data "recorde.txt;." --icon="cobra.ico" cobra_principal.py


Certifique-se de que o arquivo cobra.ico está na pasta do projeto.


🤝 Contribuições
Quer colaborar com o projeto? Sinta-se à vontade para abrir uma issue ou enviar um pull request. Sugestões de melhorias, novos modos de jogo ou efeitos sonoros são super bem-vindos!
