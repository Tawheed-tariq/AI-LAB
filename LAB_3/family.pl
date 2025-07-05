%% Exercise 2.3 Here is a tiny lexicon and mini grammar with only one rule which
%% defines a sentence as consisting of five words: an article, a noun, a verb,
%% and again an article and a noun.

word(article,a).
word(article,every).
word(noun,criminal).
word(noun,'big kahuna burger').
word(verb,eats).
word(verb,likes).

sentence(Word1,Word2,Word3,Word4,Word5) :-
  word(article,Word1),
  word(noun,Word2),
  word(verb,Word3),
  word(article,Word4),
  word(noun,Word5).

%% What query do you have to pose in order to find out which sentences the
%% grammar can generate? List all sentences that this grammar can generate in
%% the order Prolog will generate them. Make sure that you understand why Prolog
%% generates them in this order.

%% ?- sentence(A, B, C, D, E). -> generates all possibilities:
%% e.g. the following is the first possibility since it uses all the first
%% examples of article, noun, verb listed.
%% A = a,
%% B = criminal,
%% C = eats,
%% D = a,
%% E = criminal ;

%% Exercise 2.4
%% Here are six English words:
%% abalone, abandon, anagram, connect, elegant, enhance.
%% They are to be arranged in a crossword puzzle like fashion in the grid given
%% below.
%%     V1V2V3
%%     _ _ _
%% H1 _______
%%     _ _ _
%% H2 _______
%%     _ _ _
%% H3 _______
%%     _ _ _

%% The following knowledge base represents a lexicon containing these words.
word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(enhance,e,n,h,a,n,c,e).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).

%% Write a predicate crosswd/6 that tells us how to fill the grid, i.e. the
%% first three arguments should be the vertical words from left to right and the
%% following three arguments the horizontal words from top to bottom.

crossword(V1,V2,V3,H1,H2,H3) :-
  %% Make the word intersect at the right places.
  %% Use _ where we don't give a fuck about variable name.
  word(H1,_,H12V12,_,H14V22,_,H16V32,_),
  word(H2,_,H22V14,_,H24V24,_,H26V34,_),
  word(H3,_,H32V16,_,H34V26,_,H36V36,_),

  word(V1,_,H12V12,_,H22V14,_,H32V16,_),
  word(V2,_,H14V22,_,H24V24,_,H34V26,_),
  word(V3,_,H16V32,_,H26V34,_,H36V36,_)
.

%% ?- crosswd(H1,H2,H3,V1,V2,V3). ->
%% H1 = abandon, H2 = elegant, H3 = enhance, V1 = abalone, V2 = anagram,
%% V3 = connect ;
%% H1 = abalone, H2 = anagram, H3 = connect, V1 = abandon, V2 = elegant,
%% V3 = enhance ;
%% false.



