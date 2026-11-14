import { useId } from 'react';
import { AsyncActionButton, type AsyncActionButtonProps } from './AsyncActionButton';

export interface ToastNoticeProps {
  visible: boolean;
  /** Only lightweight, non-action-required results belong here. */
  kind: 'success' | 'info';
  message: string;
  onDismiss: () => void;
  /** Move to the original action or another valid target before removal. */
  restoreFocus: () => void;
  dismissLabel?: string;
  className?: string;
}

/** Keep this component mounted; update visible/message after a real result. */
export function ToastNotice({
  visible,
  kind,
  message,
  onDismiss,
  restoreFocus,
  dismissLabel = 'Dismiss notification',
  className,
}: ToastNoticeProps) {
  return (
    <div className={className} data-feedback="toast" data-kind={kind} data-visible={visible}>
      <div role="status" aria-live="polite" aria-atomic="true">
        {visible ? message : null}
      </div>
      {visible && (
        <button
          type="button"
          onClick={(event) => {
            if (event.currentTarget === event.currentTarget.ownerDocument.activeElement) {
              restoreFocus();
            }
            onDismiss();
          }}
        >
          {dismissLabel}
        </button>
      )}
    </div>
  );
}

export interface PersistentAlertProps {
  title: string;
  message: string;
  kind?: 'error' | 'warning' | 'info';
  /** Visual Alert does not imply interrupting every update. */
  announcement?: 'polite' | 'urgent';
  action?: AsyncActionButtonProps;
  className?: string;
}

/** No expiry or automatic dismissal; the owner clears only resolved issues. */
export function PersistentAlert({
  title,
  message,
  kind = 'error',
  announcement = 'polite',
  action,
  className,
}: PersistentAlertProps) {
  const titleId = useId();
  return (
    <section className={className} data-feedback="alert" data-kind={kind} aria-labelledby={titleId}>
      <div role={announcement === 'urgent' ? 'alert' : 'status'} aria-atomic="true">
        <h2 id={titleId}>{title}</h2>
        <p>{message}</p>
      </div>
      {action && <AsyncActionButton {...action} />}
    </section>
  );
}
