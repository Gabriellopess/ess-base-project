import { When, Then } from "@badeball/cypress-cucumber-preprocessor";

// Scenario: teste de busca por artista
//Given: common-step-definitions.ts
//Then: common-step-definitions.ts
//When: common-step-definitions.ts

//Scenario: Busca por nome de música/álbum
//Given: common-step-definitions.ts
//Then: common-step-definitions.ts
//When: common-step-definitions.ts

// Scenario: teste de busca por ano
//Given: common-step-definitions.ts
//Then: common-step-definitions.ts

When(
  'o usuário clica no botão {string} e preenche o campo {string} com {string} e clica no botão {string}',
  (button: string, field: string, value: string, button2: string) => {
    cy.getDataCy(button).click();
    cy.getDataCy(field).type(value);
    cy.getDataCy(button2).click();
  }
);

// Scenario: Busca com os três filtros juntos
//Given: common-step-definitions.ts
//Then: common-step-definitions.ts

When(
  'o usuário clica no botão {string} e seleciona a opção "Pop" no dropdown de gênero',
  (button: string) => {
    cy.getDataCy(button).click();
    cy.get('[data-cy=GenreButton]').select('Pop');
  }
);

When(
  'o usuário preenche o campo {string} com {string} e preenche o campo {string} com {string}',
  (field1: string, value1: string, field2:string, value2:string) => {
    cy.getDataCy(field1).type(value1);
    cy.getDataCy(field2).type(value2);
  }
);

When(
  'o usuário clica no botão {string}',
  (button: string) => {
    cy.getDataCy(button).click();
  }
);



// Scenario: teste de busca inválida
//Given: common-step-definitions.ts

When(
  'o usuário preenche o input {string} com {string} e clica no botão {string}',
  (field: string, value: string, button: string) => {
    cy.getDataCy(field).type(value);
    cy.getDataCy(button).click();
  }
);
Then('o usuário deve ver a mensagem de erro na tela', () => {
  cy.get('[data-testid=ErrorContainer]').should('be.visible');
  cy.get('[data-testid=ErrorMsg]').should('contain.text', 'Oooops! Parece que estamos enfrentando problemas ao localizar sua pesquisa.');
  cy.get('[data-testid=ErrorOtherMsg]').should('contain.text', 'Tente refazer a busca.');
});

// Scenario: teste de busca por gênero
//Given: common-step-definitions.ts

When('o usuário clica no botão {string} e seleciona a opção "Pop" no dropdown de gênero e clica no botão {string}', 
  (button1: string, button2: string) => {
  cy.getDataCy(button1).click();
  cy.get('[data-cy=GenreButton]').select('Pop');
  cy.getDataCy(button2).click();
});

Then('o usuário deve ver a música {string} e a música {string} e a música {string} na tela', 
  (musicTitle1: string, musicTitle2: string, musicTitle3: string) => {
  cy.getDataCy(musicTitle1).should("contain", "Lover");
  cy.getDataCy(musicTitle2).should("contain", "Flowers");
  cy.getDataCy(musicTitle3).should("contain", "Vampire");
});