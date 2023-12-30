# Projeto "Go Sleep: Fechamento Rápido de Programas"

## Descrição

O projeto "Go Sleep" foi desenvolvido para proporcionar aos usuários uma maneira rápida e eficiente de fechar vários programas comumente utilizados ao desligar o computador. Ele automatiza o processo de fechamento de programas, especialmente aqueles que podem estar em segundo plano ou minimizados na bandeja do sistema.

## Funcionalidades

- **Fechamento Rápido:** O projeto permite fechar rapidamente programas específicos com apenas alguns cliques.

- **Procura na Bandeja do Sistema:** Utiliza a biblioteca `pygetwindow` para procurar programas na bandeja do sistema, garantindo que até mesmo programas minimizados ou em segundo plano sejam identificados e fechados.

## Como Usar

1. **Adaptação ao Seu Uso:** Abra o arquivo `GoSleep.py` e, na seção final, adicione os nomes dos programas que deseja fechar. Por padrão, estão listados "Discord", "Steam" e "Firefox". Personalize conforme sua necessidade.

2. **Execução do Script:** Execute o script `GoSleep.py`. Ele fechará automaticamente os programas especificados.

3. **Pausa no Encerramento:** Após o fechamento dos programas, o console aguardará uma entrada do usuário antes de ser fechado. Isso permite verificar se todos os programas foram encerrados corretamente.

## NOTA

### O projeto ja vem com um executavel, por padrao está os meus programas mas voce pode personalizar a sua escolha

## Requisitos

- Python 3.x
- Bibliotecas: `pygetwindow`, `pyautogui`

Instale as bibliotecas usando:

```bash
pip install pygetwindow pyautogui
