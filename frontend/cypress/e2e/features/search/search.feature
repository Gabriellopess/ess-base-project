Feature: Busca por filtros

Scenario: Busca por artista
  Given o usuário está na página "search"
  When o usuário preenche o campo "SearchInput" com "Taylor Swift" e clica no botão "SearchButton"
  Then o usuário deve ver a música "Lover" na tela

Scenario: Busca por nome de música/álbum
  Given o usuário está na página "search"
  When o usuário preenche o campo "SearchInput" com "Lover" e clica no botão "SearchButton"
  Then o usuário deve ver a música "Lover" na tela

Scenario: Busca com os três filtros juntos
  Given o usuário está na página "search"
  When o usuário clica no botão "FilterButton" e seleciona a opção "Pop" no dropdown de gênero 
  When o usuário preenche o campo "SearchInput" com "Olivia Rodrigo" e preenche o campo "SerchYear" com "2021" 
  When o usuário clica no botão "SearchButton"
  Then o usuário deve ver a música "Drivers License" na tela

Scenario: Busca por ano
  Given o usuário está na página "search"
  When o usuário clica no botão "FilterButton" e preenche o campo "SerchYear" com "2023" e clica no botão "SearchButton"
  Then o usuário deve ver a música "Vampire" na tela

Scenario: Busca invalida
  Given o usuário está na página "search"
  When o usuário preenche o input "SearchInput" com "Mila" e clica no botão "SearchButton"
  Then o usuário deve ver a mensagem de erro na tela

Scenario: Busca por gênero
  Given o usuário está na página "search"
  When o usuário clica no botão "FilterButton" e seleciona a opção "Pop" no dropdown de gênero e clica no botão "SearchButton"
  Then o usuário deve ver a música "Lover" e a música "Flowers" e a música "Vampire" na tela