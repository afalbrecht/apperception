
%------------------------------------------------------------------------------
% Definitions for the abstract letter objects.
%------------------------------------------------------------------------------

%------------------------------------------------------------------------------
% Typing
%------------------------------------------------------------------------------

is_given_concept(p_first_letter).
is_given_concept(p_succ).
is_given_concept(p_less).
is_concept(p_first_letter).
is_concept(p_succ).
is_concept(p_less).

permanent(isa(t_letter, obj_letter_a)).
permanent(isa(t_letter, obj_letter_b)).
permanent(isa(t_letter, obj_letter_c)).
permanent(isa(t_letter, obj_letter_d)).
permanent(isa(t_letter, obj_letter_e)).
permanent(isa(t_letter, obj_letter_f)).

permanent(isa(t_letter_a, obj_letter_a)).
permanent(isa(t_letter_b, obj_letter_b)).
permanent(isa(t_letter_c, obj_letter_c)).
permanent(isa(t_letter_d, obj_letter_d)).
permanent(isa(t_letter_e, obj_letter_e)).
permanent(isa(t_letter_f, obj_letter_f)).

permanent(isa(p_first_letter, obj_letter_a)).

%------------------------------------------------------------------------------
% Pure permanent facts
%------------------------------------------------------------------------------

permanent(isa2(p_succ, obj_letter_a, obj_letter_b)).
permanent(isa2(p_succ, obj_letter_b, obj_letter_c)).
permanent(isa2(p_succ, obj_letter_c, obj_letter_d)).
permanent(isa2(p_succ, obj_letter_d, obj_letter_e)).
permanent(isa2(p_succ, obj_letter_e, obj_letter_f)).

permanent(isa2(p_less, X, Y)) :- permanent(isa2(p_succ, X, Y)).


%rule_body(r1,isa2(p_succ,X,Y)).
%rule_arrow_head(r1,isa2(p_less,X,Y)).

permanent(isa2(p_less, X, Y)) :- 
  permanent(isa2(p_succ, X, Z)),
  permanent(isa2(p_less, Z, Y)).

%:- 
%  permanent(isa(p_first_letter, Y)),
%  permanent(isa2(p_succ, X, Y)).

%:- 
%  permanent(isa2(p_less, Y, X)),
%  permanent(isa2(p_succ, X, Y)).

%rule_body(r2,isa2(p_succ,X,Z)).
%rule_body(r2,isa2(p_less,Z,Y)).
%rule_arrow_head(r2,isa2(p_less,X,Y)).

%rule_body(r1,isa2(p_succ,var_l,var_l2)).
%rule_body(r1,s2(c_letter,var_s,var_l2)).
%rule_head_causes(r1,s2(c_letter,var_s,var_l)).

