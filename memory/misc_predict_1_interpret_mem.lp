% misc_predict_1
% Optimization:19

% Typing
is_type(t_cell).
is_type(t_grid).
is_type(t_object).
is_type(t_sensor_1).
permanent(isa(t_cell,obj_sensor_a)).
permanent(isa(t_grid,obj_grid)).
permanent(isa(t_object,obj_grid)).
permanent(isa(t_object,obj_sensor_a)).
permanent(isa(t_sensor_1,obj_sensor_a)).

% Concepts
is_concept(c_a).
is_concept(c_b).
is_concept(c_c).
is_concept(c_d).
is_concept(c_off).
is_concept(c_on).
is_concept(c_part).
is_concept(t_cell).
is_concept(t_grid).
is_concept(t_object).
is_concept(t_sensor_1).

% New permanents

% Given permanents

% Rules
rule_body(r1,s(c_off,var_sensor_1_1)).
rule_head_causes(r1,s(c_on,var_sensor_1_1)).

rule_body(r2,s(c_on,var_object_1)).
rule_head_causes(r2,s(c_off,var_object_1)).

rule_body(r3,s(c_off,var_object_1)).
rule_head_causes(r3,s(c_on,var_object_1)).

rule_body(r4,s(c_on,var_sensor_1_1)).
rule_head_causes(r4,s(c_off,var_sensor_1_1)).

rule_body(r5,s(c_d,var_object_1)).
rule_head_causes(r5,s(c_a,var_object_1)).

rule_body(r6,s(c_c,var_object_1)).
rule_head_causes(r6,s(c_d,var_object_1)).

rule_body(r7,s(c_a,var_object_1)).
rule_head_causes(r7,s(c_b,var_object_1)).

rule_body(r8,s(c_b,var_object_1)).
rule_head_causes(r8,s(c_c,var_object_1)).



