:- set_prolog_flag(encoding,iso_latin_1).

say(Word, L1):-
   Goal =.. [Word,X],
   findall(X, Goal,L),
   remove_redundancies(L,L1).
   
% Chatbot Ontology for the transportation
% transportation(X):- passenger(X).
% transportation(X):- vehicle(X).

% Yolcu
% passenger(X):- paid(X).
% passenger(X):- free(X).

% Vasıta
% vehicle(X):- airplane(X).
% vehicle(X):- metro(X).
% vehicle(X):- metrobus(X).
% vehicle(X):- tram(X).
% vehicle(X):- flying_taxi(X).
% vehicle(X):- autonomous_car(X).
% vehicle(X):- taxi(X).
% vehicle(X):- midibus(X).
% vehicle(X):- train(X).
% vehicle(X):- ferry(X).

vehicle(X):- city_bus(X).
vehicle(X):- public_bus(X).
vehicle(X):- minibus(X).




