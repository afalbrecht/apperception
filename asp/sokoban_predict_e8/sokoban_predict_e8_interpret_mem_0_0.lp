% sokoban_predict_e8

% Permanents
permanent(isa(p_is_not_wall,obj_cell_1_1)).
permanent(isa2(p_below,obj_cell_1_1,obj_cell_1_2)).
permanent(isa2(p_right,obj_cell_1_1,obj_cell_2_1)).
permanent(isa(p_is_not_wall,obj_cell_1_2)).
permanent(isa2(p_below,obj_cell_1_2,obj_cell_1_3)).
permanent(isa2(p_right,obj_cell_1_2,obj_cell_2_2)).
permanent(isa(p_is_not_wall,obj_cell_1_3)).
permanent(isa2(p_below,obj_cell_1_3,obj_cell_1_4)).
permanent(isa2(p_right,obj_cell_1_3,obj_cell_2_3)).
permanent(isa(p_is_not_wall,obj_cell_1_4)).
permanent(isa2(p_right,obj_cell_1_4,obj_cell_2_4)).
permanent(isa(p_is_not_wall,obj_cell_2_1)).
permanent(isa2(p_below,obj_cell_2_1,obj_cell_2_2)).
permanent(isa2(p_right,obj_cell_2_1,obj_cell_3_1)).
permanent(isa(p_is_not_wall,obj_cell_2_2)).
permanent(isa2(p_below,obj_cell_2_2,obj_cell_2_3)).
permanent(isa2(p_right,obj_cell_2_2,obj_cell_3_2)).
permanent(isa(p_is_not_wall,obj_cell_2_3)).
permanent(isa2(p_below,obj_cell_2_3,obj_cell_2_4)).
permanent(isa2(p_right,obj_cell_2_3,obj_cell_3_3)).
permanent(isa(p_is_not_wall,obj_cell_2_4)).
permanent(isa2(p_right,obj_cell_2_4,obj_cell_3_4)).
permanent(isa(p_is_not_wall,obj_cell_3_1)).
permanent(isa2(p_below,obj_cell_3_1,obj_cell_3_2)).
permanent(isa2(p_right,obj_cell_3_1,obj_cell_4_1)).
permanent(isa(p_is_not_wall,obj_cell_3_2)).
permanent(isa2(p_below,obj_cell_3_2,obj_cell_3_3)).
permanent(isa2(p_right,obj_cell_3_2,obj_cell_4_2)).
permanent(isa(p_is_not_wall,obj_cell_3_3)).
permanent(isa2(p_below,obj_cell_3_3,obj_cell_3_4)).
permanent(isa2(p_right,obj_cell_3_3,obj_cell_4_3)).
permanent(isa(p_is_not_wall,obj_cell_3_4)).
permanent(isa2(p_right,obj_cell_3_4,obj_cell_4_4)).
permanent(isa(p_is_not_wall,obj_cell_4_1)).
permanent(isa2(p_below,obj_cell_4_1,obj_cell_4_2)).
permanent(isa(p_is_not_wall,obj_cell_4_2)).
permanent(isa2(p_below,obj_cell_4_2,obj_cell_4_3)).
permanent(isa(p_is_not_wall,obj_cell_4_3)).
permanent(isa2(p_below,obj_cell_4_3,obj_cell_4_4)).
permanent(isa(p_is_not_wall,obj_cell_4_4)).

% Rules
rule_body(r1,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r1,s(c_south,var_1_1)).
rule_body(r1,s2(c_in_1,var_1_1,var_cell_1)).
rule_head_causes(r1,s2(c_in_1,var_1_1,var_cell_2)).

rule_body(r2,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r2,s(c_north,var_1_1)).
rule_body(r2,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r2,s2(c_in_1,var_1_1,var_cell_1)).

rule_body(r3,isa(p_is_not_wall,var_cell_1)).
rule_body(r3,isa2(p_right,var_cell_2,var_cell_1)).
rule_body(r3,s(c_east,var_1_1)).
rule_body(r3,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r3,s2(c_in_1,var_1_1,var_cell_1)).

rule_body(r4,isa2(p_right,var_cell_1,var_cell_2)).
rule_body(r4,s(c_west,var_1_1)).
rule_body(r4,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r4,s2(c_in_1,var_1_1,var_cell_1)).

