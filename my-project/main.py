from manim import *

class Demo(Scene):
    def construct(self):
        # Define colors
        input_color = BLUE
        hidden_color = GREEN
        output_color = RED
        edge_color = GRAY

        # Define node radius
        node_radius = 0.3

        # Define layers
        input_layer_size = 3
        hidden_layer_size = 4
        output_layer_size = 2

        # Define positions of layers
        x_input = -4
        x_hidden = 0
        x_output = 4

        # Create nodes
        input_nodes = [Circle(radius=node_radius, color=input_color, fill_opacity=1) for _ in range(input_layer_size)]
        hidden_nodes = [Circle(radius=node_radius, color=hidden_color, fill_opacity=1) for _ in range(hidden_layer_size)]
        output_nodes = [Circle(radius=node_radius, color=output_color, fill_opacity=1) for _ in range(output_layer_size)]

        # Position nodes
        for i, node in enumerate(input_nodes):
            node.move_to([x_input, (i - (input_layer_size - 1) / 2) * 1.5, 0])
        for i, node in enumerate(hidden_nodes):
            node.move_to([x_hidden, (i - (hidden_layer_size - 1) / 2) * 1.5, 0])
        for i, node in enumerate(output_nodes):
            node.move_to([x_output, (i - (output_layer_size - 1) / 2) * 1.5, 0])

        # Create edges
        edges = []
        for input_node in input_nodes:
            for hidden_node in hidden_nodes:
                edge = Line(input_node.get_center(), hidden_node.get_center(), color=edge_color)
                edges.append(edge)
        for hidden_node in hidden_nodes:
            for output_node in output_nodes:
                edge = Line(hidden_node.get_center(), output_node.get_center(), color=edge_color)
                edges.append(edge)

        # Animation
        self.play(
            *[Create(node) for node in input_nodes],
            *[Create(node) for node in hidden_nodes],
            *[Create(node) for node in output_nodes],
            run_time=1
        )

        self.play(*[Create(edge) for edge in edges], run_time=2)

        # Input data example
        input_values = [0.2, 0.5, 0.9]
        input_texts = [Text(str(value), font_size=20) for value in input_values]
        for i, text in enumerate(input_texts):
            text.move_to(input_nodes[i].get_center() + RIGHT * (node_radius + 0.3))
            self.play(Write(text), run_time=0.5)

        # Activation animation (example)
        self.wait(0.5)
        self.play(
            *[node.animate.set_fill(color=YELLOW) for node in hidden_nodes],
            run_time=1
        )
        self.wait(0.5)
        self.play(
            *[node.animate.set_fill(color=output_color) for node in output_nodes],
            run_time=1
        )
        self.wait(1)

        # Group all elements
        all_mobjects = VGroup(*input_nodes, *hidden_nodes, *output_nodes, *edges, *input_texts)

        # Transformation: Move the entire network to the right
        self.play(all_mobjects.animate.shift(LEFT * 2), run_time=2)

        self.wait(1)
