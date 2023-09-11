import styled from "styled-components";

export const SearchMainDiv = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column; /* Adicionando uma direção de coluna */
  padding-left: 33%;
`;

export const SearchFilterWrapper = styled.div`
  display: flex;
  align-items: center;
  background-color: #f0f0f0;
  padding: 5px;
  border-radius: 40px;
  width: 100%;
  max-width: 700px;
  margin-bottom: 20px; /* Adicionando margem abaixo do SearchFilterWrapper */
`;

export const SearchInput = styled.input`
  width: 90%;
  padding: 5px 5px 5px 12px;
  border: none;
  border-radius: 40px;
  background-color: transparent;
  font-size: 16px;

  // O '&:focus' é o mesmo que 'SearchInput:focus' (se não me engano, é uma funcionalidade do styled-components)
  &:focus-visible,
  :focus {
    border: none;
    outline: none;
    box-shadow: none;
  }
`;

export const FilterButton = styled.button`
  background-color: transparent;
  border: none;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10%;

  position: relative;
`;

export const FilterImage = styled.img`
  background-color: transparent;
  border: none;
  width: 20px;
  cursor: pointer;
`;
export const LupaImage = styled.img`
  background-color: transparent;
  border: none;
  width: 30px;
  cursor: pointer;
`;


export const DropdownFilter = styled.div`
  position: absolute;
  top: 22px;

  flex-direction: column;
  align-items: start;
  justify-content: center;
  text-align: left;

  background-color: pink;

  border-radius: 10px;
  padding: 10px;
  width: 150px;
`;

export const Results = styled.div`
  display: flex;
  flex-direction: column; /* Colocar os resultados em uma coluna */
  margin-top: 20px; /* Adicionar algum espaçamento acima dos resultados */
  width: 100%; /* Fazer com que a largura dos resultados seja igual à largura do componente pai */
  //margin-left: 20%;
`;

export const ResultItem = styled.div`
  margin-bottom: 10px; /* Adicionar algum espaçamento entre os itens de resultado */
`;
