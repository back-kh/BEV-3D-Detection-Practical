import onnx
import onnx_graphsurgeon as gs
import numpy as np

def modify_onnx_input_shape(model_path, output_path, new_shape):
    """Modify the input shape of an ONNX model."""
    model = onnx.load(model_path)
    graph = gs.import_onnx(model)

    for input_tensor in graph.inputs:
        input_tensor.shape = new_shape

    graph.cleanup().toposort()
    onnx.save(gs.export_onnx(graph), output_path)
    print(f"Saved modified ONNX model to {output_path}")

def remove_reshape_nodes(model_path, output_path):
    """Remove reshape nodes from the ONNX model."""
    model = onnx.load(model_path)
    graph = gs.import_onnx(model)

    for node in graph.nodes:
        if node.op == "Reshape":
            graph.nodes.remove(node)

    graph.cleanup().toposort()
    onnx.save(gs.export_onnx(graph), output_path)
    print(f"Saved model with removed reshape nodes to {output_path}")
