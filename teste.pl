:- use_module(library(db)).
:- csv_load('position.csv', 'name').

evidence(name(X)).

0.355::risk :- name(bls),name(tls).
0.555::risk :- name(bls),\+name(tls).

0.555::risk :- name(bls),\+name(tls).

0.5::heads(C).
two_heads :- heads(c1), heads(c2).

query(risk).
