from pathlib import Path
import pandas as pd

INPUT_FILE = Path("data/raw/sample_sales.csv")
CLEANED_OUTPUT = Path("data/processed/cleaned_sales.csv")
REPORTS_DIR = Path("reports")

def load_sales_data(file_path: Path) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    return pd.read_csv(file_path)

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize sales data."""
    cleaned = df.copy()
    
    cleaned['date'] = pd.to_datetime(cleaned["date"], errors="coerce")
    cleaned['quantity'] = pd.to_numeric(cleaned["quantity"], errors='coerce').fillna(0.0)
    cleaned['unit_price'] = pd.to_numeric(cleaned["unit_price"], errors='coerce').fillna(0.0)
    cleaned['payment_status'] = cleaned["payment_status"].str.strip().str.lower()
    cleaned['category'] = cleaned["category"].str.strip().str.lower()
    cleaned['product'] = cleaned["product"].str.strip().str.lower()
    cleaned['customer'] = cleaned["customer"].str.strip().str.lower()

    cleaned = cleaned.dropna(subset=['date'])
    cleaned['total_amount'] = cleaned["quantity"] * cleaned["unit_price"]
    cleaned['month'] = cleaned["date"].dt.to_period('M').astype(str)
    
    return cleaned

def generate_reports(df: pd.DataFrame) -> None:
    """Generate business reports from cleaned sales data."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    paid_sales = df[df["payment_status"] == "paid"].copy()

    monthly_sales = paid_sales.groupby("month", as_index=False).agg(
        total_revenue=("total_amount", "sum"),
        total_orders=("order_id", "count"),
        total_items_sold=("quantity", "sum")
    ).sort_values("month")
    
    category_summary = (
        paid_sales.groupby("category", as_index=False).agg(
            total_revenue=("total_amount", "sum"),
            total_orders=("order_id", "count"),
            total_items_sold=("quantity", "sum")
        ).sort_values("total_revenue", ascending=False)
    )

    customer_summary = (
        paid_sales.groupby("customer", as_index=False).agg(
            total_spent=("total_amount", "sum"),
            total_orders=("order_id", "count"),
        )
        .sort_values("total_spent", ascending=False)
    )

    monthly_sales.to_csv(REPORTS_DIR / "monthly_sales_report.csv", index=False)
    category_summary.to_csv(REPORTS_DIR / "category_sales_report.csv", index=False)
    customer_summary.to_csv(REPORTS_DIR / "customer_sales_report.csv", index=False)


def main():
    raw_data = load_sales_data(INPUT_FILE)
    cleaned_df = clean_sales_data(raw_data)
    CLEANED_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(CLEANED_OUTPUT, index=False)
    generate_reports(cleaned_df)
    print("Automation finished successfully.")
    print(f"Cleaned data saved to: {CLEANED_OUTPUT}")
    print(f"Reports saved to: {REPORTS_DIR}")


if __name__ == "__main__":
    main()
