% sokoban_predict_e4
% Optimization:17

% Typing
is_type(t_1).
is_type(t_cell).
is_type(t_object).
permanent(isa(t_1,obj_x1)).
permanent(isa(t_cell,obj_cell_1_1)).
permanent(isa(t_cell,obj_cell_1_2)).
permanent(isa(t_cell,obj_cell_1_3)).
permanent(isa(t_cell,obj_cell_2_1)).
permanent(isa(t_cell,obj_cell_2_2)).
permanent(isa(t_cell,obj_cell_2_3)).
permanent(isa(t_cell,obj_cell_3_1)).
permanent(isa(t_cell,obj_cell_3_2)).
permanent(isa(t_cell,obj_cell_3_3)).
permanent(isa(t_cell,obj_cell_4_1)).
permanent(isa(t_cell,obj_cell_4_2)).
permanent(isa(t_cell,obj_cell_4_3)).
permanent(isa(t_cell,obj_cell_5_1)).
permanent(isa(t_cell,obj_cell_5_2)).
permanent(isa(t_cell,obj_cell_5_3)).
permanent(isa(t_object,obj_cell_1_1)).
permanent(isa(t_object,obj_cell_1_2)).
permanent(isa(t_object,obj_cell_1_3)).
permanent(isa(t_object,obj_cell_2_1)).
permanent(isa(t_object,obj_cell_2_2)).
permanent(isa(t_object,obj_cell_2_3)).
permanent(isa(t_object,obj_cell_3_1)).
permanent(isa(t_object,obj_cell_3_2)).
permanent(isa(t_object,obj_cell_3_3)).
permanent(isa(t_object,obj_cell_4_1)).
permanent(isa(t_object,obj_cell_4_2)).
permanent(isa(t_object,obj_cell_4_3)).
permanent(isa(t_object,obj_cell_5_1)).
permanent(isa(t_object,obj_cell_5_2)).
permanent(isa(t_object,obj_cell_5_3)).
permanent(isa(t_object,obj_x1)).

% Concepts
is_concept(c_east).
is_concept(c_in_1).
is_concept(c_noop).
is_concept(c_north).
is_concept(c_south).
is_concept(c_west).
is_concept(east).
is_concept(in_1).
is_concept(in_2).
is_concept(noop).
is_concept(north).
is_concept(p_below).
is_concept(p_is_not_wall).
is_concept(p_is_wall).
is_concept(p_right).
is_concept(south).
is_concept(t_1).
is_concept(t_cell).
is_concept(t_object).
is_concept(west).

% New permanents

% Given permanents
permanent(isa(p_is_not_wall,obj_cell_1_1)).
permanent(isa(p_is_not_wall,obj_cell_1_2)).
permanent(isa(p_is_not_wall,obj_cell_1_3)).
permanent(isa(p_is_not_wall,obj_cell_2_1)).
permanent(isa(p_is_not_wall,obj_cell_2_2)).
permanent(isa(p_is_not_wall,obj_cell_2_3)).
permanent(isa(p_is_not_wall,obj_cell_3_1)).
permanent(isa(p_is_not_wall,obj_cell_3_2)).
permanent(isa(p_is_not_wall,obj_cell_3_3)).
permanent(isa(p_is_not_wall,obj_cell_4_1)).
permanent(isa(p_is_not_wall,obj_cell_4_2)).
permanent(isa(p_is_not_wall,obj_cell_4_3)).
permanent(isa(p_is_not_wall,obj_cell_5_1)).
permanent(isa(p_is_not_wall,obj_cell_5_2)).
permanent(isa(p_is_not_wall,obj_cell_5_3)).
permanent(isa2(p_below,obj_cell_1_1,obj_cell_1_2)).
permanent(isa2(p_below,obj_cell_1_2,obj_cell_1_3)).
permanent(isa2(p_below,obj_cell_2_1,obj_cell_2_2)).
permanent(isa2(p_below,obj_cell_2_2,obj_cell_2_3)).
permanent(isa2(p_below,obj_cell_3_1,obj_cell_3_2)).
permanent(isa2(p_below,obj_cell_3_2,obj_cell_3_3)).
permanent(isa2(p_below,obj_cell_4_1,obj_cell_4_2)).
permanent(isa2(p_below,obj_cell_4_2,obj_cell_4_3)).
permanent(isa2(p_below,obj_cell_5_1,obj_cell_5_2)).
permanent(isa2(p_below,obj_cell_5_2,obj_cell_5_3)).
permanent(isa2(p_right,obj_cell_1_1,obj_cell_2_1)).
permanent(isa2(p_right,obj_cell_1_2,obj_cell_2_2)).
permanent(isa2(p_right,obj_cell_1_3,obj_cell_2_3)).
permanent(isa2(p_right,obj_cell_2_1,obj_cell_3_1)).
permanent(isa2(p_right,obj_cell_2_2,obj_cell_3_2)).
permanent(isa2(p_right,obj_cell_2_3,obj_cell_3_3)).
permanent(isa2(p_right,obj_cell_3_1,obj_cell_4_1)).
permanent(isa2(p_right,obj_cell_3_2,obj_cell_4_2)).
permanent(isa2(p_right,obj_cell_3_3,obj_cell_4_3)).
permanent(isa2(p_right,obj_cell_4_1,obj_cell_5_1)).
permanent(isa2(p_right,obj_cell_4_2,obj_cell_5_2)).
permanent(isa2(p_right,obj_cell_4_3,obj_cell_5_3)).

% Rules
rule_body(r10,isa2(p_right,var_cell_1,var_cell_2)).
rule_body(r10,s(c_east,var_1_1)).
rule_body(r10,s2(c_in_1,var_1_1,var_cell_1)).
rule_head_causes(r10,s2(c_in_1,var_1_1,var_cell_2)).

rule_body(r11,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r11,s(c_south,var_1_1)).
rule_body(r11,s2(c_in_1,var_1_1,var_cell_1)).
rule_head_causes(r11,s2(c_in_1,var_1_1,var_cell_2)).

rule_body(r12,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r12,s(c_north,var_1_1)).
rule_body(r12,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r12,s2(c_in_1,var_1_1,var_cell_1)).

rule_body(r5,isa2(p_right,var_cell_1,var_cell_2)).
rule_body(r5,s(c_west,var_1_1)).
rule_body(r5,s2(c_in_1,var_1_1,var_cell_2)).
rule_head_causes(r5,s2(c_in_1,var_1_1,var_cell_1)).