import React from "react";
import { MusicContainer, MusicImg, MusicArtist, MusicName, MusicRating } from "./style";

const MusicCard: React.FC<{
  artist: string;
  name: string;
  image: string;
  average_rating: number;
}> = ({ artist, name, image, average_rating}) => {
  return (
    <MusicContainer>
      <MusicImg src={image} alt="Music" />
      <MusicName>{name}</MusicName>
      <MusicArtist>{artist}</MusicArtist>
      {average_rating && <MusicRating>{average_rating}</MusicRating>}
    </MusicContainer>
  );
};

export default MusicCard;
