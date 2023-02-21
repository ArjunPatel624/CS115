#Arjun Patel
# Lab 0: PicoBot Maze Challange

#"I pledge my honnor that I have abided by the Stevens Honor System"- Arjun Patel


# Maze one solution ( Empty room)

#Get PicoBot at the top-left corner given any initial point

0 x*** -> N 0 "Go north"
0 N*x* -> W 0 "Once PicoBot hits a wall North, go West"
0 N*W* -> X 1 "Once PicoBot hits a wall North and West (Corner), change to state 1" 

#Make PicoBot move down and to the left to cover each column

1 ***x -> S 1 "Move South (downwards)" 
1 ***S -> E 2 "Once PicoBot hits a wall South, Go East and change to state 2" 

#Make PicoBot move upwards

2 x*** -> N 2 "Once PicoBot moves East, PicoBot must move bakc up to the top"
2 N*** -> E 1 " When PicoBot reaches the top, PicoBot should go East and move downwards in the next row" 


# Maze two solution (Maze)

0 **x* -> W 3 "When a space to the West is open, PicoBot will go West and stay in state 3"
0 **W* -> X 1 "When a space to the west is occupied / blocked, PicoBot will stop and go to state 1"

1 ***x -> S 0 "If a space is avaliable to the South, then PicoBot will go South and stay in state 0"
1 ***S -> X 2 "If a space to the South is occupied/blocked, PicoBot will stop and go to state 2" 

2 *x** -> E 1 "When a space to the East is open, PicoBot will go East and saty in state 1"
2 *E** -> X 3 "When a space to the East is occupied/blocked, PicoBot will stop and go to state 3"

3 x*** -> N 2 "If a space is avaliable to the North, then PicoBot will go North and stay in state 2"
3 N*** -> X 0 "If a space to the North is occupied/blocked, PicoBot will stop and go to state 0"






