
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import Dataset
from utils import load_dataset

def fine_tune_gpt2(dataset_path, model_output_dir):
    """
    Fine-tunes GPT-2 on the phonetic-to-text mapping dataset.
    """
    # Load dataset
    dataset = load_dataset(dataset_path)  # Custom function to load and preprocess dataset
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Tokenize dataset
    def tokenize_function(examples):
        return tokenizer(examples["phonetic"], examples["text"], truncation=True, padding="max_length")

    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=model_output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # Fine-tune the model
    trainer.train()
    trainer.save_model(model_output_dir)

if __name__ == "__main__":
    dataset_path = "data/phonetic_transcriptions"  # Path to phonetic-to-text dataset
    model_output_dir = "models/gpt2_finetuned"
    fine_tune_gpt2(dataset_path, model_output_dir)
