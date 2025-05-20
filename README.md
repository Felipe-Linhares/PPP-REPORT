# PPP Generator

## Descrição
Aplicação desktop para geração e gerenciamento de relatórios PPP (Progresso, Planos, Problemas).

## Características

- **Visualização em Tempo Real**: Veja seu relatório formatado enquanto digita
- **Gerenciamento de Data**: 
  - Calendário integrado para seleção de data
  - Preenchimento automático da data atual
- **Gerenciamento de Squad**:
  - Seleção de squad pré-configurada
  - Capacidade de adicionar novos squads
  - Lista de squads ordenada alfabeticamente
- **Seções do Relatório**:
  - Progressos
  - Planos
  - Problemas
- **Opções de Exportação**:
  - Copiar para área de transferência
  - Salvar como arquivo texto
  - Saída formatada automaticamente

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Felipe-Linhares/PPP-REPORT.git
cd PPP-REPORT
```

2. Crie um ambiente virtual:
```bash
python -m venv env
```

3. Ative o ambiente virtual:
```bash
.\env\Scripts\activate
```

4. Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

## Dependências

- Python 3.x
- tkinter
- tkcalendar

## Estrutura do Projeto

```
GUI/
├── src/
│   ├── __init__.py      # Inicialização do pacote
│   ├── constants.py     # Constantes da aplicação
│   ├── utils.py         # Funções utilitárias
│   └── ui.py           # Implementação principal da UI
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

## Uso

1. Inicie a aplicação:
```bash
python main.py
```

2. Preencha os campos necessários:
   - Data (preenchida automaticamente com a data atual)
   - Squad (selecione do dropdown ou adicione novo)
   - Número/nome da Sprint

3. Adicione conteúdo nas respectivas abas:
   - PROGRESSOS
   - PLANOS
   - PROBLEMAS

4. A visualização do relatório é atualizada automaticamente

## Formato do Relatório

```
PPP REPORT
DATA: DD/MM/YYYY
SQUAD: NomeDoSquad
SPRINT(s): NumeroSprint
===========
PROGRESSOS
- Item de progresso 1.
- Item de progresso 2.
===========
PLANOS
- Item de plano 1.
- Item de plano 2.
===========
PROBLEMAS
- Item de problema 1.
- Item de problema 2.
```

## Autor

[Felipe Linhares](https://github.com/Felipe-Linhares)

## Versão

- 1.0.0
  - Lançamento inicial
  - Geração básica de relatório PPP
  - Gerenciamento de squad
  - Capacidade de salvar arquivo

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Links

- Repositório do Projeto: [https://github.com/Felipe-Linhares/PPP-REPORT](https://github.com/Felipe-Linhares/PPP-REPORT)
- Reportar Bugs: [https://github.com/Felipe-Linhares/PPP-REPORT/issues](https://github.com/Felipe-Linhares/PPP-REPORT/issues)