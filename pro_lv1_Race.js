function solution(players, callings) {

  for (calling of callings) {
      let idx = players.indexOf(calling);
      let player_a = players[idx-1];
      // let player_b = players[idx];
      players[idx-1] = calling;
      players[idx] = player_a;
  };
  
  return players;
}