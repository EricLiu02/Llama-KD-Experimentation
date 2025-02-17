from transformers import AutoTokenizer, AutoModelForCausalLM, PreTrainedTokenizerFast

tokenizer = PreTrainedTokenizerFast(tokenizer_file="Bitnet B1 Tokenizer.json")
model = AutoModelForCausalLM.from_pretrained("1bitLLM/bitnet_b1_58-large", trust_remote_code=True)
