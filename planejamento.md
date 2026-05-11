- [x] Front:
    - [x] terminal
        - [x] ver tarefas (abrir o temp.md)
        - [x] resetar agenda
        - [x] sair
    - [x] temp.md 
        - [x] quando sair (abrir o terminal) 

- [ ] Back:
    - [ ] ver tarefas:
        - [ ] para abrir o temp.md:
            - [ ] resetar as tarefas quando mudar o dia
            - [x] validar tarefas.json
            - [x] ordenar as listas por diário, semanal, mensal, anual, outras listas, notas
            - [x] ordenar por lista não feitos, prazo nome
            - [x] botar as listas do banco de dados no bloco de notas
            - [x] abrir um bloco de notas quando iniciar o programa

        - [x] rodando o temp.md:
            - [x] tarefas periódicas:
                - [x] base
                    - [x] diário
                    - [x] semanal
                    - [x] mensal
                    - [x] anual
                    - [x] estrutura:
                        ```
                            [diario/semanal/mensal/anual] ([data de refresh]):
                                - [ ] [nome da tarefa]
                        ```
                - [x] outras frequencias
                    - [x] diário
                    - [x] semanal
                    - [x] mensal
                    - [x] anual
                    - [x] estrutura:
                        ```
                            a cada [quantidades] [dias/semanasmeses/anos] ([data de refresh]):
                                - [ ] [nome da tarefa]
                        ```
            - [x] tarefas não periódicas:
            ```
                sem prazo:
                - [ ] [nome da tarefa]
            ```
        - [x] para fechar o temp.md:
            - [x] validar o bloco de notas
            - [x] salvar o bloco no json
    - [x] resetar agenda
        - [x] resetar tarefa por tarefa periódica
        - [x] excluir tarefas não periódicas feitas
        - [x] ordenar tarefas
        - [x] salvar

- [x] banco:
    - [x] json
        - [x] dia de hoje
        - [x] listas de tarefas