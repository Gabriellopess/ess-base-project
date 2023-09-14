Feature: Deletar conteúdo
  As a usuário
  I want to deletar um conteúdo
  so that eu possa atualizar meu sistema

Scenario: Deletar um review
  Given o usuário está na página "edition" 
  When o usuário clica na aba "review"
  When o usuário clica em "delete_6509af1adcd79ddfd3c21898"
  When o usuário clica em "deletar" para confirmar a remoção
  Then o modal é fechado e o usuário clica em "ok" na mensagem de sucesso

Scenario: Deletar uma música
  Given o usuário está na página "edition" 
  When o usuário clica na aba "music"
  When o usuário clica em "delete_6509af0cdcd79ddfd3c21897"
  When o usuário clica em "deletar" para confirmar a remoção 
  Then o modal é fechado e o usuário clica em "ok" na mensagem de sucesso

Scenario: Deletar um album
  Given o usuário está na página "edition" 
  When o usuário clica na aba "Album"
  When o usuário clica em "delete_6509af00dcd79ddfd3c21896"
  When o usuário clica em "deletar" para confirmar a remoção 
  Then o modal é fechado e o usuário clica em "ok" na mensagem de sucesso