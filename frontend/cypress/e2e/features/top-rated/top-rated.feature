Feature: Melhores Avaliadas

Scenario: Exibir melhores avaliadas
    Given o usuário está na página "/"
    When o usuário clica no "top-rated"
    Then o usuário deve ser à pagina "top-rated" e ver a música "Borderline"

Scenario: Exibir detalhes da musica a partir do melhores avaliadas
    Given o usuário está na página "top-rated"
    When o usuário clica na imagem "https://cdn.discordapp.com/attachments/860578533159993359/1153470364509274193/tame-impala-the-slow-rush-2-1280C39710241.png"
    Then o usuário deve ver o modal "Detalhes da música"