#version 330

#if defined VERTEX_SHADER

in vec3 in_pos;
in vec3 in_color; 

out vec3 v_color;

void main() {
  v_color = in_color;
  gl_Position = vec4(in_pos, 1.0);
}

#elif defined FRAGMENT_SHADER

in vec3 v_color;

out vec4 f_color;

void main() {
  // Implicit type conversion from int to float will happen here
  f_color = vec4(v_color, 1.0);
}

#endif
