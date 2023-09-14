import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

// Scenario: Criar um test
// Given: common-step-definitions.ts

When("o usuário clica no {string}", (button: string) => {
  cy.getDataCy(button).click();
});

Then(
  "o usuário deve ser redirecionado à página {string} e visualizar os reviews com títulos {string} e {string}",
  (page: string, title: string, title2: string) => {
    cy.visit(page);
    cy.getDataCy(title).should("contain", title);
    cy.getDataCy(title2).should("contain", title2);
  }
);