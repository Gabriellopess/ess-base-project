Feature: Available on

Scenario: Verificar disponibilidade da música no Youtube a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://www.youtube.com/watch?v=RlPNh_PBZb4&ab_channel=OliviaRodrigoVEVO"