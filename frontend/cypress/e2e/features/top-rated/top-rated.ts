import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

//Given está em common-step-definitions.ts
When("o usuário clica no {string}", (button: string) => {
  cy.getDataCy(button).click();
});

Then("o usuário deve ser à pagina {string} e ver a música {string}", (page: string, song1: string, song2: string) => {
  // Verifique se o URL atual é o esperado
  cy.url().should('include', page);

  // Verifique se o título da música está sendo exibido na página
  cy.contains(song1).should('be.visible');
});


// Scenario: Usuario clica na imagem de uma música e vê o modal com os detalhes da música

When("o usuário clica na imagem {string}", (cover: string) => {
  cy.getDataCy(cover).click();
});

Then("o usuário deve ver o modal {string}", (modalName: string) => {
  cy.contains('Detalhes da música').should('be.visible');
});