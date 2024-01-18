% sw_predict_4
% Optimization:23

% Typing
is_type(t_cell).
is_type(t_grid).
is_type(t_letter).
is_type(t_object).
is_type(t_sensor).
permanent(isa(t_cell,obj_gen_1)).
permanent(isa(t_cell,obj_gen_2)).
permanent(isa(t_grid,obj_grid)).
permanent(isa(t_letter,obj_letter_a)).
permanent(isa(t_letter,obj_letter_b)).
permanent(isa(t_letter,obj_letter_c)).
permanent(isa(t_letter,obj_letter_d)).
permanent(isa(t_letter,obj_letter_e)).
permanent(isa(t_letter,obj_letter_f)).
permanent(isa(t_letter_a,obj_letter_a)).
permanent(isa(t_letter_b,obj_letter_b)).
permanent(isa(t_letter_c,obj_letter_c)).
permanent(isa(t_letter_d,obj_letter_d)).
permanent(isa(t_letter_e,obj_letter_e)).
permanent(isa(t_letter_f,obj_letter_f)).
permanent(isa(t_object,obj_gen_1)).
permanent(isa(t_object,obj_gen_2)).
permanent(isa(t_object,obj_grid)).
permanent(isa(t_object,obj_sensor)).
permanent(isa(t_sensor,obj_sensor)).

% Concepts
is_concept(c_letter).
is_concept(c_part_s).
is_concept(c_x).
is_concept(c_y).
is_concept(p_first_letter).
is_concept(p_less).
is_concept(p_p1).
is_concept(p_p2).
is_concept(p_part_c).
is_concept(p_r).
is_concept(p_succ).
is_concept(t_cell).
is_concept(t_grid).
is_concept(t_letter).
is_concept(t_object).
is_concept(t_sensor).

% New permanents
permanent(isa(p_p1,obj_gen_1)).
permanent(isa(p_p2,obj_gen_2)).
permanent(isa2(p_part_c,obj_gen_1,obj_grid)).
permanent(isa2(p_part_c,obj_gen_2,obj_grid)).
permanent(isa2(p_r,obj_gen_1,obj_gen_2)).
permanent(isa2(p_r,obj_gen_2,obj_gen_1)).

% Given permanents
permanent(isa(p_first_letter,obj_letter_a)).
permanent(isa2(p_less,obj_letter_a,obj_letter_b)).
permanent(isa2(p_less,obj_letter_a,obj_letter_c)).
permanent(isa2(p_less,obj_letter_a,obj_letter_d)).
permanent(isa2(p_less,obj_letter_a,obj_letter_e)).
permanent(isa2(p_less,obj_letter_a,obj_letter_f)).
permanent(isa2(p_less,obj_letter_b,obj_letter_c)).
permanent(isa2(p_less,obj_letter_b,obj_letter_d)).
permanent(isa2(p_less,obj_letter_b,obj_letter_e)).
permanent(isa2(p_less,obj_letter_b,obj_letter_f)).
permanent(isa2(p_less,obj_letter_c,obj_letter_d)).
permanent(isa2(p_less,obj_letter_c,obj_letter_e)).
permanent(isa2(p_less,obj_letter_c,obj_letter_f)).
permanent(isa2(p_less,obj_letter_d,obj_letter_e)).
permanent(isa2(p_less,obj_letter_d,obj_letter_f)).
permanent(isa2(p_less,obj_letter_e,obj_letter_f)).
permanent(isa2(p_succ,obj_letter_a,obj_letter_b)).
permanent(isa2(p_succ,obj_letter_b,obj_letter_c)).
permanent(isa2(p_succ,obj_letter_c,obj_letter_d)).
permanent(isa2(p_succ,obj_letter_d,obj_letter_e)).
permanent(isa2(p_succ,obj_letter_e,obj_letter_f)).

% Rules
rule_body(r1,isa2(p_less,var_l,var_l2)).
rule_body(r1,s2(c_part_s,var_s,var_c)).
rule_body(r1,s2(c_x,var_s,var_l)).
rule_body(r1,s2(c_y,var_c,var_l2)).
rule_arrow_head(r1,s2(c_letter,var_s,var_l)).

rule_body(r2,isa2(p_r,var_c,var_c2)).
rule_body(r2,s2(c_part_s,var_s,var_c2)).
rule_head_causes(r2,s2(c_part_s,var_s,var_c)).

rule_body(r3,isa(p_p1,var_c)).
rule_body(r3,isa2(p_succ,var_l,var_l2)).
rule_body(r3,s2(c_letter,var_s,var_l)).
rule_body(r3,s2(c_part_s,var_s,var_c)).
rule_head_causes(r3,s2(c_x,var_s,var_l2)).



