Feature: Available on

Scenario: Verificar disponibilidade da música na Apple Music a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://music.apple.com/br/album/vampire/1694386825?i=1694386830"


Scenario: Verificar disponibilidade da música no Youtube a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://www.youtube.com/watch?v=RlPNh_PBZb4&ab_channel=OliviaRodrigoVEVO"

Scenario: Verificar disponibilidade da música no Deezer a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://www.deezer.com/br/track/2440763155"

Scenario: Verificar disponibilidade da música no Spotify a partir do em alta
  Given o usuário está na página "in-high"
  When o usuário clica na imagem "https://hollywoodlife.com/wp-content/uploads/2023/06/Olivia-Rodrigo-Vampire-ftr.jpg?w=620"
  Then o usuário deve clicar no link "https://open.spotify.com/intl-pt/track/3k79jB4aGmMDUQzEwa46Rz?autoplay=true"