% misc_predict_1
% Optimization:5

% Typing
is_type(t_object).


permanent(isa(t_object,obj_sensor_a)).

% Concepts
is_concept(c_off).
is_concept(c_on).
is_concept(t_object).

% New permanents

% Given permanents
permanent(isa(t_object,obj_sensor_a)).

% Rules
rule_body(r1,s(c_on,var_x)).
rule_head_causes(r1,s(c_off,var_x)).

rule_body(r2,s(c_off,var_x)).
rule_head_causes(r2,s(c_on,var_x)).


% Input exclusions 
% Every object is either c_on or c_off

% At most one 
:-
    holds(s(c_on, X), T),
    holds(s(c_off, X), T).

% At least one
:-
    permanent(isa(t_object, X)),
    is_time(T),
    not holds(s(c_on, X), T),
    not holds(s(c_off, X), T).

% Incompossibility
incompossible(s(c_on, X), s(c_off, X)) :-
    permanent(isa(t_object, X)).

exclusion_output("c_on+c_off").

