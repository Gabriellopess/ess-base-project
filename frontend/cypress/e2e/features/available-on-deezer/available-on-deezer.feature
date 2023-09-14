Feature: Available on

Scenario: Verificar disponibilidade da música no Deezer a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://www.deezer.com/br/track/2440763155"