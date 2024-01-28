% misc_predict_4
% Optimization:11

% Typing
is_type(t_grid).
is_type(t_letter).
is_type(t_object).
is_type(t_sensor).
permanent(isa(t_grid,obj_grid)).
permanent(isa(t_letter,obj_letter_a)).
permanent(isa(t_letter,obj_letter_b)).
permanent(isa(t_letter,obj_letter_c)).
permanent(isa(t_letter,obj_letter_d)).
permanent(isa(t_letter,obj_letter_e)).
permanent(isa(t_letter,obj_letter_f)).
permanent(isa(t_object,obj_grid)).
permanent(isa(t_object,obj_sensor)).
permanent(isa(t_sensor,obj_sensor)).

% Concepts
is_concept(c_letter).
is_concept(p_part).
is_concept(p_succ).
is_concept(t_grid).
is_concept(t_letter).
is_concept(t_object).
is_concept(t_sensor).

% New permanents
permanent(isa2(p_part,obj_sensor,obj_grid)).
permanent(isa2(p_succ,obj_letter_a,obj_letter_f)).
permanent(isa2(p_succ,obj_letter_b,obj_letter_a)).
permanent(isa2(p_succ,obj_letter_c,obj_letter_b)).
permanent(isa2(p_succ,obj_letter_d,obj_letter_c)).
permanent(isa2(p_succ,obj_letter_e,obj_letter_d)).
permanent(isa2(p_succ,obj_letter_f,obj_letter_e)).

% Given permanents

% Rules
rule_body(r1,isa2(p_succ,var_l,var_l2)).
rule_body(r1,s2(c_letter,var_s,var_l2)).
rule_head_causes(r1,s2(c_letter,var_s,var_l)).



