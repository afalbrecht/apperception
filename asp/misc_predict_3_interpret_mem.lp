% misc_predict_3

% Permanents

% Rules
rule_body(r1,s(c_d,var_object_1)).
rule_head_causes(r1,s(c_a,var_object_1)).

rule_body(r2,s(c_c,var_object_1)).
rule_head_causes(r2,s(c_d,var_object_1)).

rule_body(r3,s(c_a,var_object_1)).
rule_head_causes(r3,s(c_b,var_object_1)).

rule_body(r4,s(c_b,var_object_1)).
rule_head_causes(r4,s(c_c,var_object_1)).

rule_body(r5,s(c_on,var_object_1)).
rule_head_causes(r5,s(c_off,var_object_1)).

rule_body(r6,s(c_off,var_object_1)).
rule_head_causes(r6,s(c_on,var_object_1)).

