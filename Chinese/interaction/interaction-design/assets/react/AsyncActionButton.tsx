import { useEffect, useRef, useState } from 'react';

export interface AsyncActionButtonProps {
  /** Stable, visible action name, for example "保存". */
  label: string;
  /** Visible state suffix; it never replaces the action name. */
  pendingLabel?: string;
  /** Return the actual operation Promise; resolving it does not create success UI. */
  onAction: () => Promise<void>;
  /** The owner renders a field error or persistent Alert, never an error Toast. */
  onRejected: (reason: unknown) => void;
  busy?: boolean;
  disabled?: boolean;
  id?: string;
  className?: string;
  describedBy?: string;
}

/** Original, unstyled action adapter. For forms, guard the form's onSubmit too. */
export function AsyncActionButton({
  label,
  pendingLabel = '处理中…',
  onAction,
  onRejected,
  busy = false,
  disabled = false,
  id,
  className,
  describedBy,
}: AsyncActionButtonProps) {
  const [localPending, setLocalPending] = useState(false);
  const inFlight = useRef(false);
  const mounted = useRef(true);
  const pending = busy || localPending;

  useEffect(() => {
    mounted.current = true;
    return () => { mounted.current = false; };
  }, []);

  async function activate() {
    if (disabled || busy || inFlight.current) return;
    // Ref guards repeated activations before React commits the next render.
    inFlight.current = true;
    setLocalPending(true);
    try {
      await onAction();
    } catch (reason) {
      onRejected(reason);
    } finally {
      inFlight.current = false;
      if (mounted.current) setLocalPending(false);
    }
  }

  return (
    <button
      type="button"
      id={id}
      className={className}
      disabled={disabled}
      aria-disabled={disabled || pending}
      aria-busy={pending}
      aria-describedby={describedBy}
      data-pending={pending || undefined}
      onClick={() => { void activate(); }}
    >
      {pending ? `${label}（${pendingLabel}）` : label}
    </button>
  );
}
