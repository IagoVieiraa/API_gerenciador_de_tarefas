# Regras de Negócio para a API REST de Gerenciamento de Tarefas

## 1. Usuários

### Cadastro de Usuário
- Um usuário deve ser capaz de se registrar no sistema com um nome, email e senha.
- O email deve ser único para cada usuário.
- A senha deve ter um mínimo de 8 caracteres e incluir pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.

### Autenticação de Usuário
- O sistema deve permitir que o usuário faça login utilizando email e senha.
- Após o login, o usuário deve receber um token JWT (JSON Web Token) para autenticação em requisições subsequentes.
- O token deve expirar após um período de inatividade (por exemplo, 30 minutos) e pode ser renovado.

### Gestão de Perfil
- O usuário deve poder atualizar suas informações de perfil, exceto o email.
- O usuário deve poder alterar sua senha, com a verificação da senha atual antes de permitir a mudança.

## 2. Tarefas

### Criação de Tarefas
- O usuário autenticado deve ser capaz de criar uma nova tarefa fornecendo um título e, opcionalmente, uma descrição, data de vencimento e prioridade.
- A data de criação deve ser automaticamente registrada.

### Atualização de Tarefas
- O usuário deve poder atualizar qualquer atributo da tarefa (título, descrição, data de vencimento, prioridade).
- O usuário não pode alterar a data de criação.

### Exclusão de Tarefas
- O usuário deve poder excluir uma tarefa existente.
- A exclusão deve ser permanente e remover todos os dados associados à tarefa.

### Visualização de Tarefas
- O usuário deve poder visualizar todas as suas tarefas.
- O usuário deve poder visualizar detalhes de uma tarefa específica por meio de um ID único.

### Listagem de Tarefas
- O usuário deve poder listar suas tarefas com opções de filtragem por data de vencimento, prioridade e status (concluída/não concluída).
- O usuário deve poder ordenar as tarefas por data de criação ou data de vencimento.

## 3. Segurança

### Autorização
- Somente o usuário que criou uma tarefa pode visualizá-la, atualizá-la ou excluí-la.
- Todas as operações de criação, atualização e exclusão de tarefas devem requerer autenticação via token JWT.

### Validação
- Todos os dados fornecidos pelo usuário devem ser validados para garantir que estão no formato correto.
- O sistema deve retornar mensagens de erro claras e apropriadas em caso de dados inválidos ou tentativas de operações não autorizadas.

## Exemplos de Endpoints

### Usuários
- `POST /api/register` - Registrar um novo usuário. - **Ainda em desenvolvimento**
- `POST /api/login` - Fazer login e receber um token JWT. - **Ainda em desenvolvimento**
- `PUT /api/profile` - Atualizar informações do perfil (exceto email). - **Ainda em desenvolvimento**
- `PUT /api/password` - Alterar a senha do usuário. - **Ainda em desenvolvimento**

### Tarefas
- `POST /api/tasks` - Criar uma nova tarefa.
- `GET /api/tasks` - Listar todas as tarefas do usuário autenticado.
- `GET /api/tasks/{id}` - Obter detalhes de uma tarefa específica. - **Ainda em desenvolvimento**
- `PUT /api/tasks/{id}` - Atualizar uma tarefa existente. - **Ainda em desenvolvimento**
- `DELETE /api/tasks/{id}` - Excluir uma tarefa existente.- **Ainda em desenvolvimento**
