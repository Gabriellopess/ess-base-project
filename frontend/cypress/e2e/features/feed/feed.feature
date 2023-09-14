Feature: Página Inicial

Scenario: Exibir reviews na página inicial
  Given o usuário está na página "/search"
  When o usuário clica no "Logo"
  Then o usuário deve ser redirecionado à página "/" e visualizar os reviews com títulos "Voltei pra os anos 2000" e "é sobre o sam e a emma!!!!"