Feature: Available on

Scenario: Verificar disponibilidade da música no Spotify a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://open.spotify.com/intl-pt/track/3k79jB4aGmMDUQzEwa46Rz?autoplay=true"