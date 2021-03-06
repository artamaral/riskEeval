:- use_module(library(db)).
:- csv_load('position.csv', 'carAT').

evidence(carAT(X)).


carAT(x).
canGo(X,Y) :- carAT(X), \+carAT(Y).


%risk evaluation from BRS POV
canGO(brs,trs).
canGO(brs,rArea).

0.7::go_rArea :- canGO(brs,trs),canGO(brs,rArea),carAT(trs),carAT(brs).

0.2::go_rArea :-
canGO(brs,trs),canGO(brs,rArea),\+carAT(trs),carAT(brs).

%risk evaluation from BLS POV
canGO(bls,tls).
canGO(bls,rArea).

0.3::go_rArea :- canGO(bls,tls),canGO(bls,rArea),
carAT(tls),carAT(bls).

0.15::go_rArea :- 
canGO(bls,tls),canGO(bls,rArea),
\+carAT(tls),carAT(bls).

%risk evaluation from C POV
canGO(c,rArea).
canGo(c,trs).
canGO(c,tls).


%the vehicle at C positions is block in both sides, so it has big probability to break and reach rArea
0.75::go_rArea :- 
canGO(c,rArea),canGo(c,trs),canGO(c,tls), carAT(c),carAT(trs),carAT(tls).

%the vehicle at C positions will accelerate to overtake a car at your right, so it`s less likely to break and reach rArea
0.25::go_rArea :- 
canGO(c,rArea),canGo(c,trs),canGO(c,tls), 
carAT(c),carAT(trs),\+carAT(tls).

0.4::go_rArea :- 
canGO(c,rArea),canGo(c,trs),canGO(c,tls), 
carAT(c),\+carAT(trs),carAT(tls).

0.15::go_rArea :- 
canGO(c,rArea),canGo(c,trs),canGO(c,tls),
 carAT(c),\+carAT(trs),\+carAT(tls).

query(go_rArea).