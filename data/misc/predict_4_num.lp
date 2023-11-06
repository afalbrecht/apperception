%------------------------------------------------------------------------------
% This is the input for learning the p_succ permanent relation.
%------------------------------------------------------------------------------

% The given sequence
senses(s2(c_number, obj_sensor, obj_number_0), 1).
senses(s2(c_number, obj_sensor, obj_number_1), 2).
senses(s2(c_number, obj_sensor, obj_number_2), 3).
senses(s2(c_number, obj_sensor, obj_number_3), 4).
senses(s2(c_number, obj_sensor, obj_number_4), 5).
senses(s2(c_number, obj_sensor, obj_number_5), 6).
senses(s2(c_number, obj_sensor, obj_number_6), 7).
senses(s2(c_number, obj_sensor, obj_number_7), 8).
senses(s2(c_number, obj_sensor, obj_number_8), 9).
hidden(s2(c_number, obj_sensor, obj_number_9), 10).

% Elements
is_object(obj_sensor).
is_time(1..10).

% Every sensor has a unique number attribute

% ∃! clause for c_number : at most one

:-
	holds(s2(c_number, X, Y), T), 
	holds(s2(c_number, X, Y2), T), 
	Y != Y2.

% ∃! clause for c_number : at least one

:-
	permanent(isa(t_sensor, X)),
	is_time(T),
	not aux_c_number(X, T).

aux_c_number(X, T) :-
	holds(s2(c_number, X, _), T).

% Incompossibility for number
incompossible(s2(c_number, X, Y), s2(c_number, X, Y2)) :-
	permanent(isa(t_sensor, X)),
	permanent(isa(t_number, Y)),
	permanent(isa(t_number, Y2)),
	Y != Y2.
