import { When, Given, Then } from "@badeball/cypress-cucumber-preprocessor";

Given(
  'o usuário está na página {string}', (page: string) => {
  cy.visit(page);
});

Then(
  'o usuário deve ver a música {string} na tela', (musicTitle: string) => {
  cy.getDataCy(musicTitle).should("contain", musicTitle);
});

When(
  'o usuário preenche o campo {string} com {string} e clica no botão {string}',
  (field: string, value: string, button: string) => {
    cy.getDataCy(field).type(value);
    cy.getDataCy(button).click();
  }
);