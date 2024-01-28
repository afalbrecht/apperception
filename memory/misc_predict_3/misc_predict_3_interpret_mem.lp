% misc_predict_3
% Optimization:14

% Typing
is_type(t_object).
permanent(isa(t_object,obj_sensor_a)).

% Concepts
is_concept(c_a).
is_concept(c_b).
is_concept(c_c).
is_concept(c_d).
is_concept(t_object).

% New permanents

% Given permanents

% Rules
rule_body(r1,s(c_a,var_object_1)).
rule_head_causes(r1,s(c_b,var_object_1)).

rule_body(r2,s(c_d,var_object_1)).
rule_head_causes(r2,s(c_a,var_object_1)).

rule_body(r3,s(c_b,var_object_1)).
rule_head_causes(r3,s(c_c,var_object_1)).

rule_body(r4,s(c_c,var_object_1)).
rule_head_causes(r4,s(c_d,var_object_1)).



