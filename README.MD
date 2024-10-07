# LlamaFile Guide: Creation, GPU Acceleration, and Server Mode

This repository accompanies a YouTube video tutorial on working with llamafiles, focusing on creation, GPU acceleration, and server mode operation. 

## What are LlamaFiles?

LlamaFiles are self-contained executables that package a language model, making it easy to run on various systems without complex setup.



## Contents

1. [Creating a LlamaFile](#creating-a-llamafile)
2. [Running with GPU Acceleration](#running-with-gpu-acceleration)
3. [Server Mode Operation](#server-mode-operation)



## Creating a LlamaFile

### Prerequisites

1. Download the latest LlamaFile release:
   - Go to the [LlamaFile GitHub releases page](https://github.com/Mozilla-Ocho/llamafile/releases)
   - Download the latest `llamafile-*.zip` for your operating system

2. Extract the ZIP file to a location of your choice

3. Temporarily add the LlamaFile `bin` directory to your system PATH:

   In your terminal (bash or similar), use the following command:
   ```
   export PATH=$PATH:/path/to/llamafile/bin
   ```
   Replace `/path/to/llamafile/bin` with the actual path to the `bin` directory in your extracted llamafile folder.

   Note: This PATH addition is temporary and will only last for the current terminal session. If you close the terminal, you'll need to run this command again.

### Creating the LlamaFile

1. Navigate to the directory containing your GGUF file:
   ```
   cd /path/to/your/gguf/file
   ```

2. Use the llamafile-convert tool:
   ```
   ./llamafile-convert your-model.gguf
   ```

This will generate a llamafile executable from your GGUF model.



## Running with GPU Acceleration

To run a llamafile using GPU acceleration:

1. Ensure you have the necessary CUDA toolkit installed (version 12.6 Update 2 or compatible version for your system).

2. Run the llamafile with the `-ngl` parameter and specify the GPU:
   ```
   ./your-llamafile.exe -ngl 9999 --gpu nvidia
   ```

   - The `-ngl 9999` argument attempts to offload as many layers as possible to the GPU.
   - The `--gpu nvidia` specifies to use the NVIDIA GPU.

3. If you encounter issues, try adjusting the number of layers or GPU parameters:
   ```
   ./your-llamafile.exe -ngl 35 --gpu nvidia
   ```
   This example tries to offload 35 layers to the GPU, which might work better on some systems.

Notes:
- If you encounter errors, check your CUDA installation and GPU compatibility.
- The optimal number of layers to offload can vary depending on your GPU model and available VRAM.
- Some systems may require additional parameters or different GPU specifications. Consult the llamafile documentation for more options.
- If you're still having issues, try running without GPU acceleration to ensure the base model works correctly.



## Server Mode Operation

To run a llamafile in server mode without opening a browser:

./your-llamafile --server --nobrowser

This starts the model in server mode, allowing you to interact with it programmatically or through custom interfaces.



## Using the Python Client Script

After setting up your llamafile in server mode, you can interact with it using the provided Python script.

### Prerequisites
- Python 3.6 or higher
- `requests` library (install with `pip install requests`)

### Steps to Use the Python Client

1. Ensure your llamafile server is running in server mode (as described in the [Server Mode Operation](#server-mode-operation) section).

2. Save the `serverlf.py` script in your desired location.

3. Open a terminal or command prompt.

4. Navigate to the directory containing `serverlf.py`:
   ```
   cd /path/to/directory/containing/serverlf.py
   ```

5. Run the script:
   ```
   python serverlf.py
   ```

6. You will see a welcome message. You can now start chatting with the AI assistant.

7. Type your messages and press Enter to send them.

8. To exit the chat, type 'exit' and press Enter.

### Customization

You can modify the `serverlf.py` script to adjust various parameters:

- `SERVER_URL`: Change this if your llamafile server is running on a different port or address.
- `SYSTEM_PROMPT`: Modify this to change the AI's behavior or role.
- `temperature` and `max_tokens` in the `send_message` function: Adjust these to change the AI's creativity and response length.

Remember to restart the Python script after making any changes.



## Additional Resources

- [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads)
- [LlamaFile Documentation](https://github.com/Mozilla-Ocho/llamafile) (official repository)



## Video Tutorial

For a detailed walkthrough of these processes, check out our YouTube video: [Link to your video]



## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements for this guide.


## License

[Specify your license here]