% misc_predict_4
% Optimization:4

% Typing
is_type(t_letter).
is_type(t_object).
is_type(t_sensor).
permanent(isa(t_letter,obj_letter_a)).
permanent(isa(t_letter,obj_letter_b)).
permanent(isa(t_letter,obj_letter_c)).
permanent(isa(t_letter,obj_letter_d)).
permanent(isa(t_letter,obj_letter_e)).
permanent(isa(t_letter,obj_letter_f)).
permanent(isa(t_sensor,obj_sensor)).

% Concepts
is_concept(c_letter).
is_concept(p_succ).
is_concept(t_letter).
is_concept(t_object).
is_concept(t_sensor).

% New permanents

% Given permanents
permanent(isa2(p_succ,obj_letter_a,obj_letter_b)).
permanent(isa2(p_succ,obj_letter_b,obj_letter_c)).
permanent(isa2(p_succ,obj_letter_c,obj_letter_d)).
permanent(isa2(p_succ,obj_letter_d,obj_letter_e)).
permanent(isa2(p_succ,obj_letter_e,obj_letter_f)).
permanent(isa2(p_succ,obj_letter_f,obj_letter_a)).

% Rules
rule_body(r1,isa2(p_succ,var_letter_1,var_letter_2)).
rule_body(r1,s2(c_letter,var_sensor_1,var_letter_1)).
rule_head_causes(r1,s2(c_letter,var_sensor_1,var_letter_2)).



