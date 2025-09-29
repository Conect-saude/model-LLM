Guia de Contribuição - Serviço de ML Conecta+Saúde
Agradecemos seu interesse em contribuir para o serviço de Machine Learning! Siga estas diretrizes para manter o projeto organizado.

💬 Fluxo de Trabalho com Pull Requests
Todo o desenvolvimento deve ser feito em branches separadas e integrado através de Pull Requests (PRs) para a branch develop.

Sincronize sua branch develop:

git checkout develop
git pull origin develop

Crie uma nova Branch: Crie uma branch a partir da develop para sua nova funcionalidade ou correção. Use os seguintes prefixos:

feature/: Para novas funcionalidades (ex: feature/adicionar-novo-modelo).

fix/: Para correções de bugs (ex: fix/corrigir-pre-processamento).

git checkout -b feature/nome-da-sua-feature

Faça seus Commits: Adicione suas alterações e faça commits com mensagens claras e descritivas.

git add .
git commit -m "feat: Adiciona novo modelo de detecção de anomalias"

Envie sua Branch: Envie sua branch para o repositório remoto.

git push -u origin feature/nome-da-sua-feature

Abra o Pull Request: No site do GitHub, crie um Pull Request da sua branch para a branch develop. Preencha o template do PR com uma descrição clara do que foi feito e como testar.

Solicite uma Revisão: Adicione pelo menos um colega de equipe como revisor do seu PR.

Obrigado pela sua colaboração!