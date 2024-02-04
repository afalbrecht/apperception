% misc_predict_3

% Permanents

% Rules
rule_body(r1,s(c_a,var_sensor_2_1)).
rule_head_causes(r1,s(c_b,var_sensor_2_1)).

rule_body(r2,s(c_d,var_sensor_2_1)).
rule_head_causes(r2,s(c_a,var_sensor_2_1)).

rule_body(r3,s(c_b,var_sensor_2_1)).
rule_head_causes(r3,s(c_c,var_sensor_2_1)).

rule_body(r4,s(c_c,var_sensor_2_1)).
rule_head_causes(r4,s(c_d,var_sensor_2_1)).

