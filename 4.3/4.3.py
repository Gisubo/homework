import multiprocessing
import time
import sys
import codecs

def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == "exit":
            output_queue.put("exit")
            break
        time.sleep(5)
        output_queue.put(message.lower())

def process_b(input_queue, result_queue):
    while True:
        message = input_queue.get()
        if message == "exit":
            result_queue.put("exit")
            break
        encoded_message = codecs.encode(message, 'rot_13')
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{timestamp}] Process B received: {encoded_message}")
        result_queue.put(encoded_message)

if __name__ == "__main__":
    queue_a = multiprocessing.Queue()
    queue_b = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    
    proc_a = multiprocessing.Process(target=process_a, args=(queue_a, queue_b))
    proc_b = multiprocessing.Process(target=process_b, args=(queue_b, result_queue))
    
    proc_a.start()
    proc_b.start()
    
    while True:
        user_input = input()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{timestamp}] Sent to Process A: {user_input}")
        queue_a.put(user_input)
        
        if user_input == "exit":
            break
    
    proc_a.join()
    proc_b.join()
    
    with open("interaction_log.txt", "w") as file:
        while not result_queue.empty():
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            message = result_queue.get()
            file.write(f"[{timestamp}] Final result: {message}\n")
