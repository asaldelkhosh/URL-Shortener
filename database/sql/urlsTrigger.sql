CREATE TRIGGER remove_unused_urls BEFORE update 
ON urls
BEGIN
    DELETE FROM urls WHERE datetime(updated_at) < datetime('now', '-7 day');
END;