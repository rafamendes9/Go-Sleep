# Projeto "Go Sleep: Fechamento Rápido de Programas"

## Descrição

O projeto "Go Sleep" foi desenvolvido para proporcionar aos usuários uma maneira rápida e eficiente de fechar vários programas comumente utilizados ao desligar o computador. Ele automatiza o processo de fechamento de programas, especialmente aqueles que podem estar em segundo plano ou minimizados na bandeja do sistema.

## Funcionalidades

- **Fechamento Rápido:** O projeto permite fechar rapidamente programas específicos com apenas alguns cliques.

- **Procura na Bandeja do Sistema:** Utiliza a biblioteca `pygetwindow` para procurar programas na bandeja do sistema, garantindo que até mesmo programas minimizados ou em segundo plano sejam identificados e fechados.

## Interface Gráfica

A interface gráfica é criada usando a biblioteca Tkinter.

- **Lista de Programas:**
  - O usuário pode selecionar programas da lista apresentada.
  - Adicione ou remova programas da lista conforme necessário.

- **Botão "Fechar Programas Selecionados":**
  - Quando pressionado, chama a função `fechar_programas_selecionados()` para fechar os programas selecionados.

- **Botão "Fechar":**
  - Fecha a interface gráfica quando pressionado.


## Como Usar

1. **Adicionar Programas:**
   - Adicione os programas desejados à lista `programas` no código.

2. **Executar o Código:**
   - Execute o script Python.
   - A interface gráfica será exibida com a lista de programas.

3. **Selecionar Programas:**
   - Selecione os programas que deseja fechar na lista.

4. **Fechar Programas:**
   - Pressione o botão "Fechar Programas Selecionados" para fechar os programas selecionados.

5. **Fechar Interface:**
   - Pressione o botão "Fechar" para fechar a interface gráfica.


## NOTA

### O projeto já vem sendo atualizado/modificado constantemente para melhor atender ao usuário. Espero que este projeto possa ajudar você tanto quanto me ajuda

## Requisitos

- Windons(7,10)
- Python 3.x
- Bibliotecas: `pygetwindow`, `pyautogui`


